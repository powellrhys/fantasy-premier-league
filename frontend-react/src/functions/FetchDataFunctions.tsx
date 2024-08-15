export async function CollectPlayerData() {
    try {
        const response = await fetch('http://localhost:8000/players?api_key=wru12!', {
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
        const response = await fetch('http://localhost:8000/leagues?api_key=wru12!', {
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
