import tweetsBySitename from "./tweets.json";

export function fetchTweets(sitename: string): Promise<types.Tweet[]> {
    return new Promise((resolve) => {
        setTimeout(() => {
            if (sitename in tweetsBySitename) {
                const tweets =
                    tweetsBySitename[sitename as keyof typeof tweetsBySitename];
                const result: types.Tweet[] = tweets.map((t) => ({
                    ...t,
                    created_at: new Date(t.created_at),
                }));
                resolve(result);
            } else {
                resolve([]);
            }
        }, 0);
    });
}
