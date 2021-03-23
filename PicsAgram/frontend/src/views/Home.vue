<template>
  <div class="home">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-10 offeset-1">
          <Post v-for="post in posts"
            :key="post.id"
            :post="post"
            @delete-post="deletePost"
          />
          <button
            v-show="next"
            class="btn btn-sm btn-success mb-5"
            @click="getPosts"
          >Carica Ancora</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import Post from "@/components/Post.vue";

export default {
  name: "Home",
  data() {
    return {
      posts: [],
      next: null,
      showComments: [],
      userHasVoted: false,
      likes_count: 0
    }
  },
  components: {
    Post
  },
  methods: {
    getPosts() {
      let endpoint = "/api/posts/";
      if(this.next) {
        endpoint = this.next
      }
      apiService(endpoint)
        .then(data => {
          this.posts.push(...data.results);
          this.next = data.next;
        })
    },
    deletePost(post) {
      let endpoint = `/api/posts/${post.id}/`;
      apiService(endpoint, "DELETE");
      this.posts.splice(this.posts.indexOf(post), 1);
    }
  },
  created() {
    this.getPosts();
            document.title = "PicsAgram - Homepage";
  }
};
</script>

<style>
html,body{
  height: 100%;
}
.author{
  color: #1d1d21;
  font-weight: bold;
}
.description{
  font-style: italic;
}
.btn:focus{
  box-shadow: none !important;
}
</style>