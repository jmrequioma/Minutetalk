new Vue({
    delimiters: ['[[', ']]'],
    el: '#home',
    data() {
        return {
            dialog: false,
            editprofile: false,
            editform: true,
            isEditing: null,
            drawer: null,
            menupopout: false,
            search_input: '',
            search_result: [],
            show_search_result: false,
            queryHTML: null,
            form: {
                fname: '',
                lname: '',
                email: '',
                username: '',
                password: '',
                cpassword: '',
                age: '',
                gender: '',
                test: '',
            },
            firstnameRules: [
                v => this.is_valid_field(v) || 'First Name is required'
            ],
            lastnameRules: [
                v => this.is_valid_field(v) || 'Last Name is required'
            ],
            usernameRules: [
                v => this.is_valid_field(v) || 'Username is required'
            ],
            passwordRules: [
                v => this.is_valid_field(v) || 'Password is required',
                v => this.is_valid_password(v) || 'Password must be or more than 8 characters'
            ],
            emailRules: [
                v => this.is_valid_email(v) || 'E-mail must be valid'
            ],
            confirmRules: [
                v => (this.is_valid_password2(v) && this.is_valid_password(password)) || 'Passwords do not match'
            ],
            ageRules: [
                v => this.is_valid_field(v) || 'Age is required',
                v => this.is_valid_age(v) || 'You must be 18 years old'
            ],

            iconlist: [{
                    title: 'Settings',
                    icon: 'settings'
                },

                {
                    title: 'Logout',
                    icon: 'exit_to_app'
                }
            ],
            user: {
                myfriends: [{
                        title: 'Mark Louis Cobo',
                        avatar: 'https://scontent.fmnl4-3.fna.fbcdn.net/v/t1.0-9/16508724_257346621359911_2391502370336370422_n.jpg?_nc_cat=0&oh=f6e2cad0a00a655f673463ac3fd2c509&oe=5BA041B1'
                    },
                    {
                        title: 'Timothy River Paler',
                        avatar: 'https://scontent.fmnl4-3.fna.fbcdn.net/v/t1.0-9/16143076_1541011595912411_6397090310466530141_n.jpg?_nc_cat=0&oh=e4ea26d2f4c31fca3178ed4d2207c734&oe=5BE31199'
                    },
                    {
                        title: 'Tehillah Leigh Lapura',
                        avatar: 'https://scontent.fmnl4-3.fna.fbcdn.net/v/t1.0-9/29027146_1896065663759969_1964858795305730048_n.jpg?_nc_cat=0&oh=634e6feff88eb698b253fd14d93e763e&oe=5BB2F176'
                    },
                    {
                        title: 'Marie Curie Salera',
                        avatar: 'https://scontent.fmnl4-3.fna.fbcdn.net/v/t1.0-9/22853443_1689141051097186_4885884491507680611_n.jpg?_nc_cat=0&oh=217127d24ad65e5ae3a53d9241e968d2&oe=5BAE5931'
                    },
                    {
                        title: 'Arvin Bonganay',
                        avatar: 'https://scontent.fmnl4-3.fna.fbcdn.net/v/t1.0-1/12745457_877244785726525_7184995272760411538_n.jpg?_nc_cat=0&oh=e49f68033dee373ea129200c5a6ab14e&oe=5BA133C2'
                    },
                    {
                        title: 'Earl Timothy Malaki',
                        avatar: 'https://scontent.fmnl4-3.fna.fbcdn.net/v/t1.0-9/34069062_2466558426703414_1702227162972553216_n.jpg?_nc_cat=0&oh=8b73a50f399d18b7b5416f240e95f6a8&oe=5B9DA59F'
                    }
                ],
            },
            display: [{
                    header: 'Music',
                    data: [{
                            title: 'Autotelic Gigs',
                            src: 'http://payload486.cargocollective.com/1/12/391449/12025306/Daniel-Behance-autotelic03_670.jpg',
                            online: '101',
                            desc: 'Lorem ipsum eu pariatur dolor et cupidatat id magna velit laborum et adipisicing nostrud sit.'
                        },
                        {
                            title: 'Paramore Tour 4',
                            src: 'https://www.billboard.com/files/media/05-paramore-press-photo-Lindsey-Byrnes-billboard-1548.jpg',
                            online: '10003',
                            desc: 'Lorem ipsum eu occaecat laboris ut proident cillum eu elit reprehenderit cillum minim.'
                        },
                        {
                            title: 'Shanti Dope-rst',
                            src: 'https://images.genius.com/7b330b6ab79b5f7efbd66e7547c40d6d.1000x525x1.jpg',
                            online: '234',
                            desc: 'Lorem ipsum officia reprehenderit id laboris velit duis qui ut minim ut anim cillum consequat est eiusmod dolore pariatur.'
                        },
                        {
                            title: 'One Directioners',
                            src: 'http://www.kiss925.com/wp-content/uploads/sites/59/2017/07/one-direction-up-all-night-album-artwork-billboard-1548-e1500836795682-1024x576.jpg',
                            online: '143',
                            desc: 'Pariatur ut ullamco dolore voluptate tempor quis esse deserunt dolor non.'
                        },
                        {
                            title: 'Chicsers Unite',
                            src: 'https://i.ytimg.com/vi/xaidwirHE10/maxresdefault.jpg',
                            online: '1',
                            desc: 'Magna velit in veniam ex ex nostrud sed ullamco qui nulla.'
                        },
                    ]
                },
                {
                    header: 'TV Series',
                    data: [{
                            title: 'Silicon Valley',
                            src: 'https://cdn-images-1.medium.com/max/1280/1*c4NYXft8lyS7bkpaaMWREQ.jpeg',
                            online: '34243',
                            desc: 'Ut occaecat ad reprehenderit mollit ut fugiat ut anim duis est aliquip voluptate excepteur aliquip.'
                        },
                        {
                            title: 'Big Bang Theory',
                            src: 'http://hotcountry1035.com/wp-content/uploads/2016/11/bbt.png',
                            online: '45345',
                            desc: 'Amet dolore amet do ut dolore occaecat nostrud deserunt cillum mollit.'
                        }, {
                            title: 'Friends',
                            src: 'https://cdn.24.co.za/files/Cms/General/d/4320/28d1220097b54f79907f2d810b51ad0b.jpg',
                            online: '5345345',
                            desc: 'Do consectetur ut officia et id qui commodo nisi pariatur reprehenderit dolor.'
                        }, {
                            title: 'How I Met Your Mother',
                            src: 'http://digitalspyuk.cdnds.net/17/20/768x384/landscape-1494944662-himym.jpg',
                            online: '123322',
                            desc: 'Adipisicing eiusmod culpa ea officia labore dolore veniam reprehenderit veniam tempor ut.'
                        }, {
                            title: 'You\'re The Worst',
                            src: 'https://cdn-static.sidereel.com/tv_shows/57394/giant_2x/281776-4.jpg',
                            online: '56234',
                            desc: 'Voluptate laborum magna minim sint ullamco id adipisicing incididunt eiusmod cupidatat ex excepteur pariatur.'
                        }, {
                            title: 'Suits',
                            src: 'https://www.thesouthafrican.com/wp-content/uploads/2017/08/suits-season-7-episode-7-696x391.jpg',
                            online: '12323',
                            desc: 'Elit deserunt occaecat velit deserunt id et ut qui laborum.'
                        },
                    ]
                }
            ]
        }

    },
    methods: {
        dropdown: function(option) {
            if (option == "Settings") {
                this.editprofile = true;
            } else if (option == "Logout") {
                window.location.href = "logout"

            }
        },
        join_channel: function(channel) {
            window.location.href = "{ url 'minutetalk:join_channel' channel }"
        },
        search: function() {
            var query = $('#search').val();
            $.ajax({
                url: '{% url "minutetalk:search_channel" %}',
                data: {
                    'query': query,
                },
                success: function(data) {
                    for (i in data.titles) {
                        console.log(data.titles[i])
                    }
                }
            });
        },
        is_valid_field: function(v) {
            return !!v
        },
        is_valid_password: function(v) {
            return v && v.length >= 8
        },
        is_valid_password2: function(v) {
            return v == this.form.password
        },
        is_valid_email: function(v) {
            return /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v)
        },
        is_valid_age: function(v) {
            return (/^\d{1,2}$/ && v >= 18)
        },
        reset: function() {
            if (this.isEditing) {
                this.form.fname = ''
                this.form.lname = ''
                this.form.email = ''
                this.form.username = ''
                this.form.password = ''
                this.form.cpassword = ''
                this.form.age = ''
                this.form.gender = ''
                this.isEditing = false;
            }
        }
    },
    watch: {
        search_input: function() {
            var a = []
            if (this.search_input.trim()) {
                $.ajax({
                    async: false,
                    url: 'ajax/search',
                    data: {
                        'query': this.search_input,
                    },
                    success: function(data) {
                        if (data.titles.length > 0) {
                            this.show_search_result = true;
                            a = data.titles;
                            console.log(a)
                            this.queryHTML = `<h1> Hello</h1>`
                        } else {
                            console.log("here")
                            this.show_search_result = false;
                        }
                    }
                });
                this.search_result = a

            }

        },
    },
    computed: {
        r() {
            console.log("computed: ")
            console.log(this.search_result);
            return this.search_result;
        }
    }
});