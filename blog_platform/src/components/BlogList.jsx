import React, { useEffect, useState } from 'react';
import { fetchPosts } from '../services/api';
import BlogCard from './BlogCard';

const BlogList = () => {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        const getPosts = async () => {
            const data = await fetchPosts();
            setPosts(data);
        };
        getPosts();
    }, []);

    return (
        <div>
            {posts.map((post) => (
                <BlogCard key={post.id} post={post} />
            ))}
        </div>
    );
};

export default BlogList;
