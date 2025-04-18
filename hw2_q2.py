from collections import namedtuple
from enum import Enum
from itertools import zip_longest

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))


def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
    updated_listing = []
    # First, we want to remove irrelevent agents ("HEALTHY","DEAD"):
    not_relevant = [agent for agent in agent_listing if agent.category in (Condition.HEALTHY, Condition.DEAD)] #saving for later
    agents = [agent for agent in agent_listing if agent.category not in (Condition.HEALTHY, Condition.DEAD)]

    pairs = zip_longest(agents[::2], agents[1::2])

    for a, b in pairs:
        if b is None:
            updated_listing.append(a)
            continue

        a_cat = a.category
        b_cat = b.category

        # Both are CURE:
        if a_cat == Condition.CURE and b_cat == Condition.CURE:
            updated_listing.extend([a, b])

        # One is CURE:
        elif a_cat == Condition.CURE:
            if b_cat == Condition.DYING:
                b = Agent(b.name, Condition.SICK)
            elif b_cat == Condition.SICK:
                b = Agent(b.name, Condition.HEALTHY)
            updated_listing.extend([a, b])

        elif b_cat == Condition.CURE:
            if a_cat == Condition.DYING:
                a = Agent(a.name, Condition.SICK)
            elif a_cat == Condition.SICK:
                a = Agent(a.name, Condition.HEALTHY)
            updated_listing.extend([a, b])

        # All rest of the mixups:
        elif a_cat == Condition.SICK:
            if b_cat == Condition.SICK:
                updated_listing.extend([
                Agent(a.name, Condition.DYING),
                Agent(b.name, Condition.DYING)
            ])
            elif b_cat == Condition.DYING:
                updated_listing.extend([
                Agent(a.name, Condition.DYING),
                Agent(b.name, Condition.DEAD)
            ])
        elif a_cat == Condition.DYING:
            if b_cat == Condition.SICK:
                updated_listing.extend([
                Agent(a.name, Condition.DEAD),
                Agent(b.name, Condition.DYING)
            ])
            elif b_cat == Condition.DYING:
                updated_listing.extend([
                    Agent(a.name, Condition.DEAD),
                    Agent(b.name, Condition.DEAD)
                    ])

        else:
            updated_listing.extend([a, b])

    # Adding non relevants:
    updated_listing.extend(not_relevant)

    return updated_listing

if __name__ == '__main__':
    # Question 2:
    agents = (
        Agent("Charles", Condition.CURE),
        Agent("Rosa", Condition.HEALTHY),
        Agent("Jake", Condition.DYING),
        Agent("Amy", Condition.SICK),
        Agent("Terry", Condition.CURE),
        Agent("Raymond", Condition.DEAD)
    )
    result = meetup(agents)
    print(f"Question 2 solution: {result}")