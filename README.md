# LocalNugetPackagePusher
Simple tool to create nuget packages and push them to a local repository so you know need to polute the organizations feed.


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

Output:
```shell
C:\Users\Alfred.Stangl\PycharmProjects\PackagePusher\venv\Scripts\python.exe C:/Users/Alfred.Stangl/PycharmProjects/PackagePusher/main.py ClinicalRelationship
Searching for Package CRISP.GRPC.ClinicalRelationships in nuget feed
nuget.exe list -s Local CRISP.GRPC.ClinicalRelationships
dotnet pack C:\Users\Alfred.Stangl\repos\crisp\CRISP-GRPC\src\CRISP.GRPC.ClinicalRelationships\CRISP.GRPC.ClinicalRelationships.csproj -p:PackageVersion=1.0.15
Pushing C:\Users\Alfred.Stangl\repos\crisp\CRISP-GRPC\src\CRISP.GRPC.ClinicalRelationships\bin\Debug\CRISP.GRPC.ClinicalRelationships.1.0.15.nupkg to Feed C:\Users\Alfred.Stangl\packages
b"Pushing CRISP.GRPC.ClinicalRelationships.1.0.15.nupkg to 'C:\\Users\\Alfred.Stangl\\packages'...\r\nYour package was pushed.\r\n"
```

![image](https://user-images.githubusercontent.com/44177617/150551239-dcdb148e-0a8f-48bc-aa5c-d6fa47e86fe5.png)

