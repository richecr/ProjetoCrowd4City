class Tweet extends HTMLElement {
    constructor(){
        super();
        this.$shadowRoot = this.attachShadow({mode: "open"});
    }

    connectedCallback() {
        this.text = this.innerHTML;
        this.render();
    }

    render() {
        let html = `
            <div>
                <p>${this.text}</p>
            </div>
        `;

        this.$shadowRoot.innerHTML += html;
    }
}

customElements.define("ps-tweet", Tweet);