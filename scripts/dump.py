import json

from region_management.libs.regions.models import Country, State, City


def run():
    count, total = 0, Country.objects.count()
    for country in Country.objects.all():
        data = []
        count += 1
        print("Load Data For country: --> ", country.name, " %d of Total: %d" % (count, total))
        # Add Country Data
        data.append({
            "pk": country.pk,
            "model": "regions.country",
            "fields": {
                "name": country.name.strip(),
                "code": country.code.strip(),
            }
        })

        for state in State.objects.filter(country=country):
            # Add State Data
            data.append({
                "pk": state.pk,
                "model": "regions.state",
                "fields": {
                    "name": state.name.strip(),
                    "code": state.code.strip(),
                    "country": state.country_id,
                }
            })

        for city in City.objects.filter(country=country):
            # Add City Data
            data.append({
                "pk": city.pk,
                "model": "regions.city",
                "fields": {
                    "name": city.name.strip(),
                    "country": city.country_id,
                    "state": city.state_id,
                    "latitude": str(city.latitude),
                    "longitude": str(city.longitude),
                }
            })

        f = open("tmp/%s.json" % country.name.lower(), "w")
        f.write(json.dumps(data, indent=4))

        print("Dumping Region Database Complete.")
