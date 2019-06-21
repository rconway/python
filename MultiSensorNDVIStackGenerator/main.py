
import eoepca

# Connect to primary platform - e.g. when running on own desktop
mainPlatform = eoepca.platform("http://main.platform.eo").authenticate("bob@home.org", "<<MY-API-KEY>>")
# Or, use the 'local' hosting platform - e.g. when running in 'cloud' platform
mainPlatform = eoepca.platform().authenticate("bob@home.org", "<<MY-API-KEY>>")

# Init supporting platforms
platA = eoepca.platform("http://platform-a.eo")
platB = eoepca.platform("http://platform-b.eo")
platC = eoepca.platform("http://platform-c.eo")

# Specify extent
extent = {
    "bbox": [ -0.489, 51.28, 0.236, 51.686 ],
    "time": [ "2018-01-01", "2018-12-31" ]
}

# Specify processes
proc1 = platA.collection("PLAT_A_DATA").coverage(extent).process("MultiSensorNDVI")
proc2 = platB.collection("PLAT_B_DATA").coverage(extent).process("MultiSensorNDVI")
proc3 = platC.collection("PLAT_C_DATA").coverage(extent).process("MultiSensorNDVI")

# Specify workflow
workflow = mainPlatform.parallel([proc1, proc2, proc3]).process("NDVIStacker")

# Get result - initiates 'lazy' execution
result = workflow.retrieve(format="geotiff", options={})
print(result)
