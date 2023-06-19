namespace types {
    interface Tweet {
        id: number;
        created_at: Date;
        text: string;
        url: string;
        opinions: string[];
        author: Author;
        attachment: Attachment;
    }

    interface Attachment {
        preview: string;
        title: string;
        url: string;
    }

    interface Author {
        name: string;
        avatar: string;
        verified: boolean;
    }
}

declare module "*.svg" {
    import React = require("react");
    export const ReactComponent: React.SFC<React.SVGProps<SVGSVGElement>>;
    const src: string;
    export default src;
}

declare module "*.json" {
    const content: string;
    export default content;
}
