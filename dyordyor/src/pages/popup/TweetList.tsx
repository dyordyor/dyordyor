import browser from "webextension-polyfill";
import { useEffect, useState } from "react";
import Tweet from "./Tweet";
import { getSiteNameFromUrl } from "@src/utils";
import { fetchTweets } from "@src/api";

const TWEET_HEIGHT = 174;
const TWEET_LIST_PADDING_Y = 12;
const POPUP_MAX_HEIGHT = 600;

function setPopupHeight(tweetsCount: number) {
    document.documentElement.style.maxHeight =
        Math.min(
            (TWEET_HEIGHT + TWEET_LIST_PADDING_Y * 2) * tweetsCount,
            POPUP_MAX_HEIGHT
        ) + "px";
}

export default function TweetList() {
    const [tweets, setTweets] = useState<types.Tweet[]>([]);

    useEffect(() => {
        browser.tabs
            .query({ active: true, currentWindow: true })
            .then(function (tabs) {
                const currentUrl = tabs[0].url;
                if (currentUrl) {
                    const sitename = getSiteNameFromUrl(currentUrl);
                    fetchTweets(sitename).then((tweets) => {
                        if (tweets.length > 0) {
                            const sortedTweets = tweets.slice();
                            sortedTweets.sort(
                                (a, b) =>
                                    b.created_at.getTime() -
                                    a.created_at.getTime()
                            );

                            setPopupHeight(sortedTweets.length);
                            setTweets(sortedTweets);
                        }
                    });
                }
            })
            .catch((e) => console.error(e));
    }, []);

    return (
        <div className="p-3">
            <div className="space-y-4">
                {tweets.map((tweet, index) => (
                    <Tweet tweet={tweet} key={index} />
                ))}
            </div>
        </div>
    );
}
