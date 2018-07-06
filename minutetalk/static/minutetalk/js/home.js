new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  data(){
  	return{
	    drawer: null,
	    menupopout: false,
	    search_input: '',
	    search_result: [],
	    show_search_result:false,
	    queryHTML: null,
	    user: {
	      	mychannels: [
				{
					title: 'Dota 2',
					avatar: 'https://steamuserimages-a.akamaihd.net/ugc/559884055410135065/429CE099233669AB4C0322F6F211053A0B589094/'
				},
				{
					title: 'Taylor Swift',
					avatar: 'https://orig00.deviantart.net/463a/f/2013/093/a/c/taylor_swift_png_icon_by_aubreyondeviantart-d60dk5k.png'
				},
				{
					title: 'Volleyball',
					avatar: 'http://www.pngmart.com/files/4/Volleyball-PNG-Free-Download.png'
				},
				{
					title: 'Power Gym',
					avatar: 'https://www.brandcrowd.com/gallery/brands/pictures/picture14268688597609.png'
				},
				{
					title: 'Marathon',
					avatar: 'http://kahunabailbonds.com/wp-content/uploads/2016/04/run-up-clipart-running-icon-on-transparent-background-md.png'
				},
				{
					title: 'Netflix and Chill',
					avatar: 'https://i0.wp.com/www.indyscan.com/wordpress/wp-content/uploads/2018/03/Netflix-Logo.png?fit=400%2C300&ssl=1'	
				}      					
	      	],
	     	myfriends: [
				{
					title: 'Mark Louis Cobo',
					avatar: 'https://scontent.fmnl4-3.fna.fbcdn.net/v/t1.0-9/16508724_257346621359911_2391502370336370422_n.jpg?_nc_cat=0&oh=f6e2cad0a00a655f673463ac3fd2c509&oe=5BA041B1'
				},
				{
					title: 'Timothy River Gwapo',
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
      	iconlist:[
      		{
	      		title: 'Settings', 
	      		icon: 'settings'
	      	},
	      	{
		      	title: 'Logout',
		      	icon: 'exit_to_app'
		    }
	  	],
  	}
  },
  methods: {
  	dropdown: function(option){
  		if(option == "Settings"){
  			console.log('Settings')
  		} else if (option == "Logout"){
        	window.location.href= "logout"
  		}
  	},
  	join_channel: function(channel_title,channel_id){
  		var channel = channel_title
  		if(channel.source){
  			window.location.href = channel.source.replace(/ /g, "_")
  		} else {
  			window.location.href = channel.replace(/ /g, "_")
  		}
	},
	search: function() {
		if(this.search_input.trim()){
			$.ajax({
				// url: '{% url "minutetalk:search_channel" %}',
				url: 'ajax/search',
				data : {
					'query' : this.search_input,
				},
				success: function (data) {
					if(data.titles.length > 0) {
						this.show_search_result = true;
						// this.search_result = data.titles;
						console.log(this.search_result)
					} else {
						this.show_search_result = false;
					}
				}
			});
		} 
	},
  },
  watch: {
  	search_input: function() {
  		var a = []
		if(this.search_input.trim()){
			$.ajax({
				async:false,
				url: 'ajax/search',
				data : {
					'query' : this.search_input,
				},
				success: function (data) {
					if(data.titles.length > 0) {
						this.show_search_result = true;
						a = data.titles;
						console.log(a)
						this.queryHTML =`<h1> Hello</h1>`
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
