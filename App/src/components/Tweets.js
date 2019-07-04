import "./Tweet.js";

class Tweets extends HTMLElement {
    constructor() {
        super();
        this.$shadowRoot = this.attachShadow({"mode": "open"});
        this.tweets = [];
        this.cont = 0;
    }

    async connectedCallback() {
        await this.render();
    }

    async render() {
        await this.api();
        console.log(this.cont);
        var d = document.createElement("div");

        let t = this.tweets[this.cont]
        let html = `
            <ps-tweet>${t.full_text}</ps-tweet>
        `;

        let $div = document.createElement("div");
        $div.innerHTML = html;

        d.appendChild($div);

        this.$shadowRoot.appendChild(d);

        var b = document.createElement("button");
        b.onclick = async () => await this.proxima();
        b.innerHTML = "Proxima";
        this.$shadowRoot.appendChild(b);
    }

    async api() {
        let response  = await fetch("../../../twitter_scraping/dados/educacao/dados.json");
        this.tweets = await response.json();
    }

    async proxima() {
        console.log("object");
        this.$shadowRoot.innerHTML = "";
        this.cont += 1;
        await this.render();
    }
}

customElements.define("ps-tweets", Tweets);