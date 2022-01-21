# LocalNugetPackagePusher

Setup ini file for each project:
- ProjectPath: Path to CSProj to Build
- LocalFeed: Path to local feed (ensure you make this directory)
- PackageName: Namespace and package name
- Path to nuget.exe (included in repo)

```ini
[ClinicalRelationship]
ProjectPath = C:\Users\User.Name\repos\crisp\CRISP-GRPC\src\CRISP.GRPC.ClinicalRelationships\CRISP.GRPC.ClinicalRelationships.csproj
LocalFeed = C:\Users\User.Name\packages
PackageName = CRISP.GRPC.ClinicalRelationships
Nuget = nuget.exe
```


Usage:
```shell
python main.py ClinicalRelationship
```
