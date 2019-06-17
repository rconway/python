import eoepca

# Connect to primary platform
tep = eoepca.platform("http://tep.eo").auth("bob@home.org", "MY-API-KEY")

# Init supporting platforms
sentinel2 = eoepca.platform("http://sentinel2.eo")
probav = eoepca.platform("http://probav.eo")
deimos = eoepca.platform("http://deimos.eo")

# Specify extent
extent = {
    "spatial": [ -0.489, 51.28, 0.236, 51.686 ],
    "temporal": [ "2018-01-01", "2018-12-31" ]
}

# Specify processes
#proc1 = sentinel2.coverage(extent).process("MultiSensorNDVI")
proc1 = sentinel2.collection("S2_DATA").coverage(extent).process("MultiSensorNDVI")
proc2 = probav.collection("PV_DATA").coverage(extent).process("MultiSensorNDVI")
proc3 = deimos.collection("DM_DATA").coverage(extent).process("MultiSensorNDVI")

# Specify workflow
workflow = tep.parallel([proc1, proc2, proc3]).process("NDVIStacker")

# Get result - initiates 'lazy' execution
result = workflow.download(format="geotiff")
print(result)
