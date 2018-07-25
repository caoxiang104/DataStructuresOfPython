from Chapter11_Sets_and_Dicts.hashtable import HashTable


class Profiler(object):
    """Represents a profiler for hash tables."""

    def __init__(self):
        self._table = None
        self._collisions = 0
        self._probeCount = 0

    def test(self, table, data):
        """Inserts the data into table and gathers statistics."""
        self._table = table
        self._collisions = 0
        self._probeCount = 0
        self._result = "Load factor    Item Inserted " + \
                       "Home Index  Actual Index   Probes\n"
        for item in data:
            loadFactor = table.loadFactor()
            table.insert(item)
            homeIndex = table.homeIndex()
            actualIndex = table.actualIndex()
            probes = table.probeCount()
            self._probeCount += probes
            if probes > 0:
                self._collisions += 1
            line = "%8.3f%14d%12d%12d%14d" % (loadFactor, item, homeIndex, actualIndex, probes)
            self._result += line + "\n"
        self._result += "Total collisions:" + str(self._collisions) + \
            "\nTotal probes:" + str(self._probeCount) + \
            "\n Average probes per collision:" + str(self._probeCount / self._collisions)

    def __str__(self):
        if self._table is None:
            return "No test has been run yet."
        else:
            return self._result


def main():
    # Create a table with 8 cells, an identity hash function and liner probing.
    table = HashTable(8, lambda x: x)
    # The data are the numbers from 10 through 70, by 10s
    data = list(range(10, 71, 10))
    profiler = Profiler()
    profiler.test(table, data)
    print(profiler)


if __name__ == '__main__':
    main()