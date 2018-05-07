# -*- coding: utf-8 -*-

import googlemaps
import geopy.distance
import pandas as pd
import numpy as np

def getLatLng(geocode_result):
    loc = geocode_result[0]['geometry']['location']
    lat = loc['lat']
    lng = loc['lng']
    return (lat, lng)

def getDist(coords1, coords2, units=None):
    if units == 'miles':
        return (geopy.distance.vincenty(coords1, coords2).miles)
    else:
        return (geopy.distance.vincenty(coords1, coords2).km)

def getAddressList():    
    address_list =  [
            'AE SAO CARLOS',
            'AHMAD MORI CLINICA RADIOLOGIA ODONTOLOGICA',
            'AMA ESPECIALIDADES VILA ZATT',
            'AMA JD PERI PERI']
    return address_list

def populateLatLng(df, gmaps):
    ref_coords = (-23.5999515, -46.7150129) # HOSPITAL ISRAELITA ALBERT EINSTEIN
    latLngDist = np.zeros((df.shape[0], 3))
    latLngDist[:] = np.nan
    for index, row in df.iterrows():
        inst = row['Institution']
        geocode = []
        geocode = gmaps.geocode(inst)
        if geocode == []:
            continue
        lat, lng = getLatLng(geocode)
        dist = getDist(ref_coords, (lat, lng), 'miles')
        latLngDist[index, :] = [lat, lng, dist]
    df['Lat'] = latLngDist[:,0]
    df['Lng'] = latLngDist[:,1]
    df['Miles from Ref'] = latLngDist[:,2]
    return df

#def main():
api_key='AIzaSyDFGsAhv47KwjjXtKlfquu7e_Ag5eQOrgg'
gmaps = googlemaps.Client(key=api_key)
df = pd.read_csv('Example.csv')
df = populateLatLng(df, gmaps)

#if __name__ == '__main__':
#    main()
