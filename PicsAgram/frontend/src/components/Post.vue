<template>
<div class="card mt-5 mb-3">

    <div class="card-header py-0">
        <div class="row my-1">
            <div class="col-6 col-sm-8 col-md-9">
                <h6 class="author pt-1">
                <router-link :to="{ name: 'profile', params: {username: post.author} }"
                >{{ post.author }}</router-link>
                </h6>
            </div>
        </div>
    </div>

    <div class="card-body text-center p-0">
        <img :src="post.image " alt="pic" style="max-width: 100%; min-width: 100%" @dblclick="addLike">
    </div>

    <div class="card-footer">
        <div class="row my-1">
            <div class="col-6 col-sm-4 col-md-8">
                <p class="description mb-0"><span class="author">{{ post.author }} </span>{{ post.description }}</p>
            </div>
            <div v-show="isOwner" class="col-6 col-sm-8 col-md-4 text-center">
                <router-link :to="{ name: 'update-post', params: {id: post.id} }"
                              class="btn btn-sm btn-outline-secondary mr-1 mb-1"
                >Modifica</router-link>
                <button
                    class="btn btn-sm btn-outline-danger mb-1"
                    @click="emitDeletePost"
                >Cancella</button>
            </div>
        </div>
        <hr class="mt-1">
        <div class="row">
            <div class="col-sm-7 col-md-8 col-lg-9">
                <i
                    class="mx-3"
                    :class="{
                    'fas fa-heart': userHasVoted,
                    'far fa-heart': !userHasVoted,
                    }"
                    @click="toggleLike"
                > [{{ likes_count }}]</i>
                <span v-if=" answersCount == 0 " class="text-muted">Commenti: {{ answersCount }}</span>
                <a v-else @click="showComments = true" class="text-muted comments-link">Commenti: {{ answersCount }}</a>
            </div>
            <div class="col-sm-5 col-md-4 col-lg-3 mt-1">
                <button 
                    @click="showForm = true"
                    class="btn btn-sm btn-outline-info"
                >Commenta</button>
            </div>
        </div>
        
        <div v-if="showForm" class="mt-2">
            <hr>
            <form @submit.prevent="submitComment">
                <textarea
                    v-model="newComment"
                    rows="3"
                    class="form-control"
                    placeholder="scrivi qui il tuo commento"
                ></textarea>
                <button
                    type="submit"
                    class="btn btn-sm btn-info mt-2"
                >Pubblica Commento</button>
            </form>
            <p class="error mt-2">{{ error }}</p>
        </div>

        <hr v-show="showComments">
        <Answers 
            v-show="showComments"
            v-for="comment in comments"
            :key="comment.id"
            :comment="comment"
            @delete-comment="deleteComment"
        />
    </div>

</div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import Answers from "@/components/Answers.vue";

export default {
    name: "Post",
    props: {
        post: {
            type: Object,
            required: true
        },
    },
    data() {
        return {
            comments: [],
            showComments: false,
            answersCount: this.post.answers_count,
            userHasVoted: this.post.user_has_liked,
            likes_count: this.post.likes_count,
            showForm: false,
            newComment: null,
            error: null
        }
    },
    computed: {
        isOwner() {
            return this.post.author === window.localStorage.getItem('username');
        }
    },
    components: {
        Answers
    },
    methods: {
        getAnswers() {
            let endpoint = `/api/posts/${this.post.id}/answers/`;
            apiService(endpoint)
                .then( data => {
                    this.comments.push(...data.results);
                })
        },
        toggleLike() {
            this.userHasVoted === true ? this.deleteLike() : this.addLike()
        },
        deleteLike() {
            let endpoint = `/api/posts/${this.post.id}/like/`;
            apiService(endpoint, "DELETE")
            this.likes_count -= 1;
            this.userHasVoted = false;
        },
        addLike() {
            let endpoint = `/api/posts/${this.post.id}/like/`;
            apiService(endpoint, "POST")
            if(!this.userHasVoted) {
                this.likes_count += 1;
                this.userHasVoted = true;
            }
        },
        submitComment() {
            if(this.newComment) {
                let endpoint = `/api/posts/${this.post.id}/answer/`;
                apiService(endpoint, "POST", { 'content': this.newComment })
                    .then( data => {
                        this.comments.unshift(data);
                    })
                    if(this.error) {
                        this.error = null;
                    }
                    this.showForm = false;
                    this.newComment = null;
                    this.showComments = true;
                    this.answersCount += 1;
            } else {
                this.error = "Non puoi lasciare vuoto il campo del commento!";
            }

        },
        deleteComment(comment) {
            let endpoint = `/api/answer/${comment.id}/`;
            apiService(endpoint, "DELETE");
            this.comments.splice(this.comments.indexOf(comment), 1);
            this.answersCount -= 1;
            if(this.answersCount == 0) {
                this.showComments = false;
            }
        },
        emitDeletePost() {
            this.$emit('delete-post', this.post);
        }
    },
    created() {
        this.getAnswers();
    }

}
</script>

<style>
.comments-link:hover{
    color: rgb(113, 129, 129) !important;
}
a:hover{
  cursor: pointer;
  text-decoration: none;
}
i:hover{
  cursor: pointer;
}
</style>