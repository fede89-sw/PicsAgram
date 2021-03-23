<template>

    <div v-if="notFoundComputed" class="container mt-4">
        <h1 class="notFound">404 - UTENTE NON TROVATO</h1>
    </div>


    <div v-else class="profile">
        <div class="container">
            <div class="row mt-4">
                <div class="col-4 text-center">
                    <img v-show="profile.profile_picture"
                         :src="profile.profile_picture"
                         alt="pic"
                         class="rounded-circle"
                         style="height: 150px; max-width: 100%; width: 160px;"
                    >
                    <p v-show="isOwner" class="pt-3">
                        <router-link :to="{ name: 'profile-picture-editor', params: {username: username} }"
                        >Modifica Foto Profilo</router-link>        
                    </p>
                </div>
                <div class="col-8">
                    <h3>{{ profile.username }}
                        <span v-show="isOwner">
                            <router-link :to="{ name: 'profile-editor', params: {username: username} }"
                                         class="btn btn-sm btn-outline-secondary ml-2"
                            >Modifica Profilo</router-link>
                        </span>
                    </h3>
                    <p>{{ profile.first_name }} {{ profile.last_name }}</p>
                    <p>{{ profile.biography }}</p>
                </div>
            </div>
            <hr class="mt-4">
            <div class="row justify-content-center">
                <div class="col-7 offeset-1">
                    <Post v-for="post in posts"
                        :key="post.id"
                        :post="post"
                        @delete-post="deletePost"
                    />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {apiService} from "@/common/api.service.js";
import Post from "@/components/Post.vue";

export default {
    name: "Profile",
    props: {
        username: {
            type: String,
            required: true
        }
    },
    components: {
        Post
    },
    computed: {
        isOwner() {
            return this.username === window.localStorage.getItem('username');
        },
        notFoundComputed() {
            return this.profile["detail"];
        }
    },
    data() {
        return {
            profile: {},
            posts: []
        }
    },
    methods: {
        getProfile() {
            let endpoint = `/api/${this.username}/`;
            apiService(endpoint)
                .then( data => {
                    this.profile = data;
                    this.posts = data.posts;
                    this.posts.reverse();
                })
        }, 
        deletePost(post) {
            let endpoint = `/api/posts/${post.id}/`;
            apiService(endpoint, "DELETE");
            this.posts.splice(this.posts.indexOf(post), 1);
        }
    },
    created() {
        this.getProfile();
        document.title = "PicsAgram - " + this.username;
    },
    updated() {
        this.getProfile();
        document.title = "PicsAgram - " + this.username;
    }
}
</script>