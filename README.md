# DataFocusedPython_Group07

File ScrappingCode is the complete version to scrap data, from the initial page to the data we need.
File Example.csv is an example of data we need to use to locate address. Note: we need to use variable 'Institution' (health care institution name) to search for its coordinates (lat, lon). I know there's a formula with which we can compute the distance only using two sets of coordinates. Otherwise, we could retrieve directly the distance (in Km) from Google Earth. Instead of comparing every institution against each other, focus on one institution ('HOSPITAL ISRAELITA ALBERT EINSTEIN') and let's find the distance of all other institutions compared to this one.


File ScrapData02 is the web scrap script for a specific health care equipment (named "Gama Camara"). Key id to use in google earth api is "Institution" which is the name of the estabilishment (hospital, especialized clinics or laboratories).
