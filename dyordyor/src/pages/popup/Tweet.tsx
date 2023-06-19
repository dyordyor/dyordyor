import { useState } from "react";
import ReactMarkdown from "react-markdown";
import Author from "./Author";
import Toggler from "./Toggler";
import { formatCreatedAt, formatAttachmentUrl } from "@src/utils";

interface TweetProps {
    tweet: types.Tweet;
}

export default function Tweet({ tweet }: TweetProps) {
    const [isOpen, setIsOpen] = useState(false);
    return (
        <div
            className="pb-4 flex space-x-4 items-start overflow-x-hidden cursor-pointer"
            onClick={() => chrome.tabs.create({ url: tweet.url })}
        >
            <img
                src={tweet.author.avatar}
                alt={tweet.author.name}
                className="h-10 w-10 rounded-full"
            />

            <div>
                <div className="flex items-center">
                    <Author author={tweet.author} />
                    <Toggler isOpen={isOpen} onChange={setIsOpen} />
                </div>
                <div className="flex">
                    <ReactMarkdown
                        className={`prose text-sm text-gray-700 text-left ${
                            isOpen ? "" : "line-clamp-2"
                        }`}
                    >
                        {tweet.text}
                    </ReactMarkdown>

                    <span className="ml-4 text-gray-500 whitespace-nowrap">
                        {formatCreatedAt(tweet.created_at)}
                    </span>
                </div>
                {tweet.opinions.length > 0 && (
                    <div className="flex mt-2">
                        <div className="flex -space-x-1 overflow-hidden">
                            {tweet.opinions.map((o) => (
                                <img
                                    className="inline-block h-4 w-4 rounded-full ring-2 ring-white"
                                    src={o}
                                    alt=""
                                    key={o}
                                />
                            ))}
                        </div>
                        <div className="ml-2 text-gray-500 text-xs">
                            {tweet.opinions.length} opinions
                        </div>
                    </div>
                )}
                <div className="mt-3 flex gap-2 relative">
                    <div className="absolute -left-4 h-full w-[1px] bg-gray-100"></div>
                    <img
                        className="w-20 aspect-video rounded-sm"
                        src={tweet.attachment.preview}
                    />
                    <div className="">
                        <div className="w-full font-semibold line-clamp-2 leading-tight">
                            {tweet.attachment.title}
                        </div>
                        <div className="mt-1 text-xs text-gray-400">
                            {formatAttachmentUrl(tweet.attachment.url)}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
