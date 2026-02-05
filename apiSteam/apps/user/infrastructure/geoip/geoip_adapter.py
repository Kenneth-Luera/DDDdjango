from django.contrib.gis.geoip2 import GeoIP2


class GeoIPAdapter:
    def get_geo_data(self, ip):
        g = GeoIP2()
        try:
            data = g.city(ip)
            return {
                "country": data.get("country_name"),
                "city": data.get("city"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
            }
        except Exception:
            return {}
