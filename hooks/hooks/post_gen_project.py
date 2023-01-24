import os

# converts groupId like com.example and artifact id like demo into a string com/example/hello 
directory = '{{ cookiecutter.__package.replace('.','/') }}'

srcDir = 'src/main/java/' + directory

# create typical maven directory structure
os.makedirs(srcDir, exist_ok=True)

# move Main.java to Maven sources
os.rename("Main.java", srcDir + '/Main.java')

# generate Maven wrapper
os.system('mvn wrapper:wrapper')

# download dependencies
os.system('./mvnw verify')