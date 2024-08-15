export async function CollectPlayerData() {
    try {
        const api_key = import.meta.env.VITE_API_KEY;
        const api_url = import.meta.env.VITE_API_URL;
        const response = await fetch(`${api_url}/players?api_key=${api_key}`, {
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

export async function CollectLeagueData() {
    try {
        const api_key = import.meta.env.VITE_API_KEY;
        const api_url = import.meta.env.VITE_API_URL;
        const response = await fetch(`${api_url}/leagues?api_key=${api_key}`, {
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
