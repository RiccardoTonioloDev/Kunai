def find_in(to_search, space):
    # PRE: to_search and space are both strings

    # Lowering the case to improve search without seeing at the case
    to_searchLW = to_search.lower()
    spaceLW = space.lower()
    # Seeing if we found to_searchLW in spaceLW
    found = to_searchLW in spaceLW
    # Returning a tuple that shows if it's found, and if found, at what index it is
    return (found, spaceLW.index(to_searchLW) if found else 0)


# USAGE
print(find_in("prova", "adsfjalsdfjaofjalkfjajfPrOvAdslfkjaflkjasfòjal"))
