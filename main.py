import phonenumbers
import opencage
import folium
from myphone import P_number 
from phonenumbers import geocoder

penumber = phonenumbers.parse(P_number)

location = geocoder.description_for_number(penumber , "en")

print(location)


from phonenumbers import carrier

service_pro = phonenumbers.parse(P_number)

print(carrier.name_for_number(service_pro , 'en'))


from opencage.geocoder import OpenCageGeocode

key = 'be6407138bc149fba3f4151fa210f585'

geo_coder = OpenCageGeocode(key)

query = str(location)

results = geo_coder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']


print(lat , lng)


myMap = folium.Map(location=[lat , lng] , zoom_start=9)

folium.Marker([lat,lng] , popup=location).add_to(myMap)

myMap.save("mylocation.html")