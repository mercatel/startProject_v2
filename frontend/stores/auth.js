import {defineStore} from 'pinia'

export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        env: useRuntimeConfig(),
        user: null,
        role: null,
        token: null,
    }),
    actions: {
        async logIn(path, body) {
            const response = await fetch(`${this.env.public.baseUrl}/auth/jwt/create/`, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(body)
            })
            if (response.status === 200) {
                const res = await response.json()
                await this.setToken(res.access, path)
            }
            return response.status
        },
        async setToken(token, patch) {
            this.token = token
            localStorage.setItem('token', token)
            return navigateTo(patch)
        },
        async initStore() {
            if (localStorage.getItem('token')) {
                this.token = localStorage.getItem('token')
                await this.initUser()
            }
            else {
                return navigateTo('/');
            }

        },
        async initUser() {
            const response = await fetch(`${this.env.public.baseUrl}/api/account-my/`, {
                headers: {
                    'Authorization': `JWT ${this.token}`,
                    'Content-Type': 'application/json'
                },
            })
            if (response.status === 200) {
                this.user = await response.json()
                this.role = this.user.role
            } else
                this.logout()

        },
        logout() {
            this.user = null
            this.token = ""
            localStorage.removeItem('token')
            return navigateTo('/');
        }
    },
    getters: {
        getUser() {
            return this.user
        }
    }
})