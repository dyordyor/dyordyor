# DYORDYOR: Crypto Community Insight
DYORDYOR aims to provide a unique slice-of-life perspective on the crypto community on Twitter. It generates readable and informative digests, summarizing key events, sentiments towards various cryptocurrencies, rising projects, and hot topics within the crypto space.

## Tech Stack
### Twitter Parsing
Our journey begins with a comprehensive collection of tweets from our pre-determined sources over the past 24 hours using a basic twitter parsing mechanism.

### Twitter Topic Analysis
The raw data from Twitter is then processed through a rudimentary analysis of the word frequency in the collected tweets. This allows us to determine the most frequently discussed topics in our dataset.

### [CVS Modulator]([url](https://github.com/dyordyor/dyordyor/blob/main/CSV%20moderator%20-%20dyordyor.ipynb))
Common words such as articles, basic verbs, and prepositions often have high mention counts. To filter out relevant crypto-specific topics, we employ a GPT-based AI tool.

### [DYORDYOR Twitter Word Filter]([url](https://github.com/dyordyor/dyordyor/blob/main/DYORDYOR%20Twitter%20Word%20Filter.py))
This tool excludes irrelevant words and retains crypto-related proper nouns from the dataset.

## Tweet Grouping and AI Analysis
The top discussion topics are then sorted into sections within a Google Sheets file by a separate script. The sections are subsequently analyzed by a GPT AI system to generate summaries, sentiment analyses, and pertinent quotes for each topic.

### [DYORDYOR AI Topic Summarization]([url](https://github.com/dyordyor/dyordyor/blob/main/DYORDYOR%20AI%20Topic%20summarization%20and%20Sentiment%20Analysis.py))
The tool that helps in summarizing, sentiment analysis, and collecting valuable quotes for each topic.

### Data Presentation
The analyzed data is presented in the following format:

| Topic | Summary + Quotes | Sentiment (Bearish, Bullish, or Neutral) |

While the table is extensive and often not immediately ready for public release, we do grant public access to it for transparency. The table is usually published on Telegra.ph.

## Finalization
We utilize the latest GPT model to format and condense the raw data into a concise format suitable for social media. The finalized summary is then shared on our social media channels.

Keep up to date with us on Telegram @dyordyorcom!
