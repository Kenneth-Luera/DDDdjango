from django.contrib.gis.geoip2 import GeoIP2
from apiSteam.apps.user.application.utils.ip import get_client_ip

def set_user_location(user, request):
    try:
        ip = get_client_ip(request)
        g = GeoIP2()

        data = g.city(ip)

        user.ip_address = ip
        user.country = data.get('country_name')
        user.city = data.get('city')
        user.latitude = data.get('latitude')
        user.longitude = data.get('longitude')

        user.save()

    except Exception as e:
        print("GeoIP error:", e)
