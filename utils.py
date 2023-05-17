def length(length_metering):
    metering = {
        'standard lenght': length_metering['lenght1'],
        'fork lenght': length_metering['lenght2'],
        'total length': length_metering['length3']
    }
    labels = metering.keys()
    values = metering.values()
    return labels, values


def length_by_fish(species):
    result = list(filter(lambda item: item['Species'], species))
    return result

