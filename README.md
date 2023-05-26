# ShenyenGPT

This app enables AI-powered search for Master Sheng Yen's Classical Lectures

This is also a testbed for exploring Langchain functionality.

- The repository is revised from  [Lex-GPT](https://github.com/PineappleExpress808/lex-gpt)

## Dataset

Scrape Master Sheng Yen's Classical Lectures from 

https://miblue119.github.io/shengyen_lectures/index.html

Transcribed data is split / embedded (Pinecone) with Langchain.

All steps outlined in: `scripts/get_shenyen_data.ipynb`

## Search

Use Langchain `VectorDBQAChain` to:

* Embed the user query
* Perform similarity search on Pinecone embeddings
* Synthesize the answer from relevant chunks with `GPT 3.5`

## Search

Relevant chunks with metadata (links) are displayed as source documents.

This builds on the excellent UI from https://github.com/mckaywrigley/wait-but-why-gpt.

## Deploy

Note: the app that supports streaming is deployed to fly.io: https://shenyen-gpt.vercel.app/

This is because Vercel requires edge functions for streaming.

We are working on getting edge functions working with Langchain.

In the meantime, use   https://shenyen-gpt.vercel.app/ for the more performant app.

## Credits

Thanks to [Mckay Wrigley](https://twitter.com/mckaywrigley) for open-sourcing his UI.
Thanks to [RLanceMartin](https://twitter.com/RLanceMartin) open source his [Lex-GPT](https://github.com/PineappleExpress808/lex-gpt)


## Contact
