// https://nuxt.com/docs/api/configuration/nuxt-config
// @ts-ignore
export default defineNuxtConfig({
    runtimeConfig: {
        public: {
            // @ts-ignore
            baseUrl: process.env.BASE_URL,
        },
    },
    modules: [
        '@pinia/nuxt', '@invictus.codes/nuxt-vuetify',
    ],
    compatibilityDate: '2024-11-01',
    devtools: {enabled: false}
})
