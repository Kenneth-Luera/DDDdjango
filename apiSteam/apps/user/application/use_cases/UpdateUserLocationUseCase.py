from apiSteam.apps.user.infrastructure.geoip.geoip_adapter import GeoIPAdapter

class UpdateUserLocationUseCase:
    def execute(self, user, ip):
        geoip = GeoIPAdapter()
        location = geoip.get_geo_data(ip)

        user.ip_address = ip
        user.country = location.get("country")
        user.city = location.get("city")
        user.latitude = location.get("latitude")
        user.longitude = location.get("longitude")
        user.save()