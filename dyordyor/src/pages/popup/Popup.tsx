import TweetList from "./TweetList";

export default function Popup() {
    return (
        <div className="absolute top-0 left-0 right-0 bottom-0 h-full">
            <TweetList />
        </div>
    );
}
