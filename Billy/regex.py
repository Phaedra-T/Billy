import re

# Predefined lists of destinations
destinations = {
    'Europe': {
        'cool': '''Iceland
When it comes to cool weather summer vacations in Europe, Iceland is among the most wishlist-worthy destinations. With natural wonders including glacier-topped volcanoes, bubbling hot springs, and tumbling waterfalls, it’s not hard to see why. This small island nation in the North Atlantic is also home to the legendary Icelandic Sagas, so there’s plenty of Viking history to uncover. What’s more, the compact capital of Reykjavík is peppered with world-class museums and has a thriving foodie scene.''',
        'sunny': '''Porto, Portugal
Portugal is one of the most amazing places for travelers who wish to spend their summer vacation in a place where they have many things to explore and discover. It is filled with marvelous architecture, delicious food, and breathtaking beaches. Once you have had your first Pastéis de Nata, a traditional Portuguese pastry, Portugal will forever have a special place in your heart.'''
    },
    'Asia': {
        'cool': '''Sapa, Vietnam
Nestled in the Hoàng Liên Son Mountains of northwestern Vietnam, Sapa is a picturesque town known for its cool climate, terraced rice fields, and rich cultural heritage. In July, Sapa experiences mild temperatures, typically ranging from 15°C to 20°C (59°F to 68°F), making it a perfect getaway. The misty valleys, lush green landscapes, and opportunities for trekking and exploring local ethnic villages add to Sapa's charm.''',
        'sunny': '''Bali, Indonesia
Nestled in the heart of Indonesia, Bali is a tropical paradise that beckons travelers from around the world. With its stunning beaches, lush rice terraces, vibrant culture, and a wide range of activities, Bali is the perfect destination for a summer getaway. In this section, we’ll explore Bali in detail and provide you with insights on how to book flights to Bali, including tips on finding cheap, affordable flights and checking airfares.'''
    },
    'North America': {
        'cool': '''Lake Tahoe, California and Nevada
Lake Tahoe is a large lake in the Sierra Nevada Mountains in both California and Nevada and one of the best places to go to beat the summer heat. In addition, it offers amazing scenery, such as forests overflowing with beautiful trees, spectacular beaches with views of Half Dome Mountain, and crystal clear blue water inviting you to swim.''',
        'sunny': '''Boston
As the largest city in New England and the birthplace of the American Revolution, Boston is undoubtedly one of the absolute best places to visit over the summer in the USA. With its coastal location, gorgeous architecture, a dizzying array of distinct neighborhoods, and world-class museums (not to mention universities), you’ll never run out of incredible things to do in Boston. That being said, thanks to the city’s dense historic center and easy-to-access attractions along the Freedom Trail, spending even one day in Boston can be incredibly rewarding.'''
    },
    'South America': {
        'cool': '''Patagonia, Argentina
Patagonia is larger than many countries around the world and is split between Argentina and Chile. You can expect each city in the region to feel unique; some of the most popular in Argentinian Patagonia are El Calafate, Ushuaia, and El Chaltén. Whether you go to Patagonia Brewery in San Carlos de Bariloche or hike one of the 300 glaciers throughout the region, you're sure to have an unforgettable experience.''',
        'sunny': '''Rio De Janeiro, Brazil
Rio de Janeiro is the capital of both Brazil and of the state of Rio de Janeiro and is commonly referred to as Rio by tourists. A trip to Brazil would be incomplete without a visit to this lovely city. Rio de Janeiro is famed for its natural environment, carnival celebrations, samba music, and other distinct styles of music. It encompasses an area of around 1,260 km². This city is well-known among tourists for its remarkable natural landscape. Therefore, it is one of the best cities to visit in South America, which includes long white sandy beaches and rainforests in the city’s center.'''
    },
    'Africa': {
        'cool': '''Cape Town
Summers can bring temperatures above 100 degrees. From June to September, however, the city rarely sees temps above 63, which is comfortable enough to hike Table Mountain to Maclear's Beacon, go whale watching, and see penguins at Boulders Beach (though don’t plan on swimming in the water — it’s frigid). On days when it’s a little too cool to be outside, there are many museums and other indoor attractions to explore, plus countless restaurants contributing to Cape Town’s reputation as a culinary capital.''',
        'sunny': '''Tanzania
Tanzania has a great mix of sights and activities for tourists to fill their itinerary. You have beaches giving you access to the Indian Ocean. Tanzanian cities also have a great mix of modern shops and local bazaars.'''
    },
    'Australia': {
        'cool': '''Tasmania
Because its position is closer than other states to Antarctica, it is the state that gets the coldest, especially when the winds pick up. Tasmania doesn’t get very hot, even in summer, but the Australian sun can still heat you up quickly when outside, ensuring beach days are still on the cards.''',
        'sunny': '''Kangaroo Island
Tranquil Kangaroo Island lies off the coast of South Australia, near Adelaide. The island is home to an estimated 65,000 kangaroos—more than 14 to each resident. This is a paradise for nature lovers as you’ll also see seals, countless seabirds, and echidnas, also known as spiny anteaters. More than a third of the island is protected as a nature reserve.'''
    }
}

# Track user choices
user_preferences = {}

# List of patterns with responses
p = [
    (r'\b(h+e+l+o+|h+i+|h+e+y+)\b', "Hello! I am Billy, your virtual trip planner! Where would you like to spend your summer vacations?"),
    (r'(.*)(tha+nk|by+e+)', "Goodbye! Have a great trip!"),
    (r'(.*)\b(europe|asia|north america|south america|africa|australia)\b', 
     lambda match: {
         'response': f"Great choice! Do you prefer a cool or sunny destination in {match.group(2).capitalize()}?",
         'continent': match.group(2).capitalize()
     }),
    (r'\b(cool|sunny)\b', 
     lambda match: {
         'response': f"Sounds great! I’d recommend {destinations[user_preferences.get('continent', '')][match.group(1).lower()]}.",
         'weather': match.group(1).lower()
     }),
    (r'(.*)(don\'t know|help|suggest|recommend|not sure)', 
     "If you want a low temperature getaway why not visit Norway? It's a great place to cool off! \nBut if you prefer nice warm weather and sunny beaches how about a trip to Hawaii? You'll love the sunshine there!")
]

# Compile the patterns with re.IGNORECASE
patterns = [(re.compile(pattern, re.IGNORECASE), response) for pattern, response in p]

def get_response(question):
    for pattern, response in patterns:
        match = pattern.search(question)
        if match:
            result = response(match) if callable(response) else response
            if isinstance(result, dict):
                if 'continent' in result:
                    user_preferences['continent'] = result['continent']
                if 'weather' in result:
                    user_preferences['weather'] = result['weather']
                return result.get('response', "I'm not sure I understand.")
            return result
    return "I'm not sure I understand. Could you please clarify?"
