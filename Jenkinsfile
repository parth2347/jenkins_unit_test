pipeline {
   agent any
   stages {
      stage('unit testing'){
          steps{
               println("Unit testing started...")
               script{

                    workspace = pwd()
                    project = "jenkins_unit_test"
                    project_path = "${workspace}/${project}"

                    dir("${workspace}/test_packages"){
                        String requirementsFilePath = "${workspace}/requirements.txt"
                        String destinationPath = "${workspace}/test_packages/"
                        pipInstall(requirementsFilePath,destinationPath)
                        main_pytest_command("${workspace}")
                    }
               }
          }
      }
   }
}

def pipInstall(String requirementsFileName, String destinationPath){

    sh "pip install -r ${requirementsFileName} -t ${destinationPath} >/dev/null"
    //Install from Pypi server also possible
}

def main_pytest_command(String directory){
    dir(directory)
    {
        //writeFile file: ".coveragerc", text: """[run] omit=**/test_packages/*"""
        sh "python -m pytest "
    }
}