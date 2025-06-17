/** @type {import('vite').UserConfig} */

const hotReloadForMarkdown = () => {
  return {
    name: "hot-reload-markdown",
    enforce: "post",
    handleHotUpdate({ file, server }) {
      if (file.endsWith(".md")) {
        server.ws.send({
          type: "full-reload",
          path: "*",
        });
      }
    },
  };
};

export default {
  plugins: [hotReloadForMarkdown()],
};
