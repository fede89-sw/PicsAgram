<template>
    <div class="container">
        <nav class="navbar navbar-expand-lg navbar-light bg-light my_navbar">
            <router-link
                class="navbar-brand"
                to="/"
            ><strong>PicsAgram</strong></router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ml-auto">
                <li v-if="!light" class="nav-item dropdown">
                    <span class="nav-link">
                        <a class="far fa-moon" @click="switchTheme('light.css')"></a>
                    </span>
                </li>
                <li v-else class="nav-item dropdown">
                    <span class="nav-link">
                        <a class="fas fa-moon" @click="switchTheme('dark.css')"></a>
                    </span>
                </li>
                <li class="nav-item dropdown">
                    <router-link
                        class="nav-link"
                        to="/post"
                    >Aggiungi Post</router-link>
                </li>
                <li class="nav-item dropdown">
                    <router-link :to="{ name: 'profile', params: {username: user} }"
                                  class="nav-link"
                    >{{ user }}</router-link>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link" href="/accounts/logout/">Logout</a>
                </li>
            </ul>
        </div>
        </nav>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
    name: "Navbar",
    data() {
        return {
            user: window.localStorage.getItem("username"),
            theme: window.localStorage.getItem("theme"),
            light: true
        }
    },
    methods: {
        async getUser() {
            let endpoint = "/api/user/";
            await apiService(endpoint)
                .then( data => {
                window.localStorage.setItem('username', data.username);
                this.user = data.username;
                })
            },
        async getTheme() {
            let endpoint = `/api/${this.user}/theme/`;
            await apiService(endpoint)
                .then( data => {
                    this.theme = data.theme;
                    document.getElementById("myTheme").href = 'http://localhost:8000/static/css/' + this.theme; 
                    if(this.theme == 'light.css'){this.light = true} else {this.light = false};             
                })
            },
        async switchTheme(theme) {
            let endpoint = `/api/${this.user}/theme/`;
            apiService(endpoint, "PUT", {theme: theme})
                .then( data => {
                    this.theme = data.theme;
                })
            document.getElementById("myTheme").href = 'http://localhost:8000/static/css/' + theme;
            window.localStorage.setItem("theme", theme);
            if(theme == 'light.css'){this.light = true} else {this.light = false};             
            }
    },
    created() {
        this.getUser();
        this.getTheme();
    }
}
</script>