param (
    [Parameter(HelpMessage = "Rebuild Container Locally")]
    [boolean]$build
)

if ($build) {
    docker build -t fpl-frontend .
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
$api_url = $environment_variables_array[3]
$api_key = $environment_variables_array[4]
$dashboard_key = $environment_variables_array[5]
$sql_server_name = $environment_variables_array[6]
$sql_server_database = $environment_variables_array[7]
$sql_server_username = $environment_variables_array[8]
$sql_server_password = $environment_variables_array[9]

Write-Host $dashboard_key

# Run Docker Container
docker run -p 8000:8000 `
    -e leagues=$leagues `
    -e manager_id=$manager_id `
    -e password=$password `
    -e api_url=$api_url `
    -e api_key=$api_key `
    -e dashboard_key=$dashboard_key `
    -e sql_server_name=$sql_server_name `
    -e sql_server_database=$sql_server_database `
    -e sql_server_username=$sql_server_username `
    -e sql_server_password=$sql_server_password `
    fpl-frontend 
