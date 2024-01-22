param (
    [Parameter(HelpMessage = "Rebuild Container Locally")]
    [boolean]$build
)

if ($build) {
    docker build -t fpl-frontend -f frontend/Dockerfile .
}

# Empty array to store environmental variables
$environment_variables_array = @()

# Iterate through .env file to retrieve terraform state file remote
# container credentials
get-content .env | foreach {
    $name, $value = $_.split('=')
    $environment_variables_array += $value.Replace("'", "")
}

# Map sourced environmental variables to correct keys
$leagues = $environment_variables_array[0]
$manager_id = $environment_variables_array[1]
$password = $environment_variables_array[2]
$sql_server_name = $environment_variables_array[3]
$sql_server_database = $environment_variables_array[4]
$sql_server_username = $environment_variables_array[5]
$sql_server_password = $environment_variables_array[6]

# Run Docker Container
docker run -p 8501:8501 `
    -e leagues=$leagues `
    -e manager_id=$manager_id `
    -e password=$password `
    -e sql_server_name=$sql_server_name `
    -e sql_server_database=$sql_server_database `
    -e sql_server_username=$sql_server_username `
    -e sql_server_password=$sql_server_password `
    fpl-frontend 
