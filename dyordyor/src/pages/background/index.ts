import browser from "webextension-polyfill";

import { fetchTweets } from "@src/api";
import { getSiteNameFromUrl } from "@src/utils";

browser.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status == "loading") {
        browser.action.setBadgeText({ text: "" });
    }

    if (changeInfo.status == "complete") {
        const currentUrl = tab.url;
        if (currentUrl) {
            const sitename = getSiteNameFromUrl(currentUrl);

            fetchTweets(sitename).then((tweets) => {
                const badgeText =
                    tweets.length > 0 ? tweets.length.toString() : "";
                browser.action.setBadgeText({ text: badgeText });
            });
        }
    }
});

browser.tabs.onActivated.addListener((activeInfo) => {
    browser.action.setBadgeText({ text: "" });
    browser.tabs
        .get(activeInfo.tabId)
        .then((tab) => {
            const currentUrl = tab.url;
            if (currentUrl) {
                const sitename = getSiteNameFromUrl(currentUrl);

                fetchTweets(sitename).then((tweets) => {
                    const badgeText =
                        tweets.length > 0 ? tweets.length.toString() : "";
                    browser.action.setBadgeText({ text: badgeText });
                });
            }
        })
        .catch((e) => console.error(e));
});
