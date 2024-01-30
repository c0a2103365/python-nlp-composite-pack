import datetime
import pandas as pd
import yaml

with open('/docker-compose.yml') as file:
    yml = yaml.load(file, Loader=yaml.FullLoader)
    names=[service for service in yml.get("services", {})]
    commands=[f"docker compose exec {name} bash" for name in names]
    time=[datetime.datetime.now() for _ in range(len(names))]
    
df=pd.DataFrame(data={"service": names, "enter shell command": commands, "generate log": time})
df.to_csv("./names.csv",index=False,encoding="utf-8_sig")