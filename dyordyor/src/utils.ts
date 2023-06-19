export function getSiteNameFromUrl(url: string): string {
    return new URL(url).hostname.split(".").slice(-2).join(".");
}

export function formatAttachmentUrl(url: string): string {
    if (url === "") {
        return "";
    }
    return getSiteNameFromUrl(url);
}

export function formatCreatedAt(date: Date): string {
    const now = new Date();
    if (now.getTime() - date.getTime() < 1000 * 60 * 60 * 24) {
        return now.getHours() - date.getHours() + "h";
    } else {
        return Intl.DateTimeFormat("en", {
            month: "short",
            day: "2-digit",
        }).format(date);
    }
}
