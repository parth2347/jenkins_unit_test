workspace = ""
pipeline {
   agent any
   stages {
      stage('unit testing'){
          steps{
               println("Unit testing started...")
               script{
                    workspace = pwd()
                    project = "jenkins_unit_test"

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
    sh "pip3 install -r ${requirementsFileName} -t ${destinationPath} >/dev/null"
    //Install from Pypi server also possible
}

def main_pytest_command(String directory){
    dir(directory)
    {
            writeFile file: ".coveragerc", text: """[run] omit=**/test_packages/*"""
            //sh "set Path=%PATH%;${directory}"
            def command = sh script: """pytest --continue-on-collection-errors --junitxml=report.xml -o junit_family=xunit2 --cov-config=${directory}/.coveragerc --cov=${directory} --cov-report=xml --ignore=test_packages"""
            
       if(fileExists("${directory}/coverage.xml")){
         cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: '**/coverage.xml', failUnhealthy: false, failUnstable: false, maxNumberOfBuilds: 0, onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
          xunit([JUnit(deleteOutputFiles: true,failIfNotNew: true, pattern: '**/report.xml', skipNoTestFiles: false, stopProcessingIfError: false)])       
       }
    }
}
