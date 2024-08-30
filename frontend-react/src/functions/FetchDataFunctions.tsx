export async function CollectPlayerData(endpoint_credentials: any) {
    try {
        const api_key = endpoint_credentials.api_key;
        const api_url = endpoint_credentials.api_url;
        const response = await fetch(`${api_url}/api/players?api_key=${api_key}`, {
            headers: {
                Accept: "application/json"
            }
        });
        const data = await response.json();
        return data;
    } catch (err: any) {
        console.log(err.message);
        throw err;
    }
}

export async function CollectLeagueData(endpoint_credentials: any) {
    try {
        const api_key = endpoint_credentials.api_key;
        const api_url = endpoint_credentials.api_url;
        const response = await fetch(`${api_url}/api/leagues?api_key=${api_key}`, {
            headers: {
                Accept: "application/json"
            }
        });
        const data = await response.json();
        return data;
    } catch (err: any) {
        console.log(err.message);
        throw err;
    }
}

export async function CollectAPICredentials(dashboard_key = '') {
    try {
        const response = await fetch(`/api/credentials?authentication_key=${dashboard_key}`, {
            headers: {
                Accept: "application/json"
            }
        });
        const data = await response.json();
        return data;
    } catch (err: any) {
        console.log(err.message);
        throw err;
    }
}

