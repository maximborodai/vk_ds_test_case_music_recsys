import numpy as np
import pandas as pd
from collections import Counter


def summary(df):
    """
    input: The function takes in a data frame
    output: It counts total number of records and unique records present in each column
    """

    print("Total number of records: ",len(df))
    for i in df.columns:
        print('Distinct {} in dataframe: {}'.format(i,len(np.unique(df[i].astype('str')))))


def count_na(df):
    """
    input: The function takes in a data frame
    output: It counts number of NA values in each column and % of NA values 
    """
    new=pd.DataFrame(df.isnull().astype('int').sum(axis=0),columns=["NA_count"])
    new['Percentage']=df.isnull().astype('int').sum(axis=0)*100/len(df)
    return new


def data_category_counter(df):
    counters = dict()
    for col in df.columns:
        counters[col] = Counter(df[col])
    return counters


def test_train_diff(train, test):
    count = dict()
    columns = set(train.columns).intersection(test.columns)
    for col in columns:
        set1 = set(train[col])
        set2 = set(test[col])
        new_item = len(set2-set1)
        count[col] = new_item
    return count


def genres_separate(genre_ids):
    """
    Each genre represented by a three-digit number, and there are songs 
    have more than one genres. We want to separate them. 
    Input: column"genre_ids" of song.csv file.
    Output: devided all possible categories existed for each of the song.
            return a dictionary where key=distinguish genre_id,
            value=number of songs belongs to that specific genre_id.
    """
    genre_dictionary = {}
    for genre_id in genre_ids:
        if type(genre_id) != str:
            continue
        genre_list = genre_id.split('|')
        for genre in genre_list:
            if genre not in genre_dictionary:
                genre_dictionary[genre] = 1
            else:
                genre_dictionary[genre] += 1
    
    return genre_dictionary  


def song_play_times(song_ids): 
    """
    We also want to know the frequencies of each song.
    input: distinct song info(ie song id).
    output: a dictionary with key=song_id, value=number of times it's played.
    or 
    We can also use a similar function for frequencies of languages.
    input: distinct language(each language represented by a different number).
    output: a dictionary with key=language, value=number of songs in this specific language.
    """
    song_play_dict = {}

    for song_id in song_ids:
        if song_id not in song_play_dict:
            song_play_dict[song_id] = 1
        else:
            song_play_dict[song_id] += 1
    
    return song_play_dict


##################################################################################################

# переводим возраст меньший либо равный нулю в nan.
# обрабатываем также и большой возраст
def age_replace(data):

    new_age = []
    for i in data['bd'].values:
        if i <= 0 :
            new_age.append(np.nan)
        elif i > 80:
            new_age.append(np.nan)
        else :
            new_age.append(i)
    data['new_bd'] = new_age
    return data


def age_replace(data):

    new_age = []
    for i in data['bd'].values:
        if i <= 0 :
            new_age.append(np.nan)
        elif i > 80:
            new_age.append(np.nan)
        else :
            new_age.append(i)
    data['new_bd'] = new_age
    return data


def get_d_m_y(sample_data):

    regi_date = sample_data['registration_init_time'].values
    expi_date = sample_data['expiration_date'].values

    day   = []
    month = []
    year  = []

    for i in regi_date:
        i = str(i)
        day.append(int(i[:4]))
        month.append(int(i[4:6]))
        year.append(int(i[6:]))
    sample_data['regi_day']   = day
    sample_data['regi_month'] = month
    sample_data['regi_year']  = year

    day   = []
    month = []
    year  = []

    for i in expi_date:
        i = str(i)
        day.append(int(i[:4]))
        month.append(int(i[4:6]))
        year.append(int(i[6:]))
    sample_data['expire_day']   = day
    sample_data['expire_month'] = month
    sample_data['expire_year']  = year

    sample_data = sample_data.drop(['expiration_date','registration_init_time'],axis =1)

    return sample_data


# function for remove columns which name start with 'Unnamed:'
# input  : dataframe
# output : dataframe without 'Unnamed:' columns
def remove_funtion(data):
    for i in data.columns:
        if i.split()[0] == 'Unnamed:':
            data = data.drop(i,axis = 1)
    return data


# function for find unique values 
# input  : dataframe
# output : list of unique values in each columns of dataframe
def info(data):
    
    columns_name = list(data.columns)
    print('columns_name',' '*(10),'unique_values' , ' '*(7),'Type' )
    print('-'*50)
    
    for name in columns_name:
        length = str(len(list(set(data[name].values)))) 
        print(name ,(25-len(name))*' ','|', length ,(10 - len(length) )*' ','|', data[name].dtype) 
    print('_'*50)
    return


# function for find missing value
# input  : dataframe
# output : percentage of missing value in each columns
# эта функция уже есть
def find_missing_values(songs_info):
    print('='*30)
    print('Shape of file :',songs_info.shape)
    print('='*30)
    print('columns_name',' '*(7),'missing_values in %')

    print('-'*30)
    
    columns_name = list(songs_info.columns)
    for name in columns_name:
        null_value = sum(songs_info[name].isnull())
        percentage = (null_value * 100) / songs_info.shape[0]
        print(name ,(25-len(name))*' ',':', percentage) 
    print('='*30)
    return


# переписать в одну в функию
# separate genre_ids and make seprate columns for each genre_ids
def separate_genre(data):
    genre = data['genre_ids'].values
    genre_category  = []

    # seprate all genre and store in genre_category
    for i in genre:
        lis = []
        i = str(i)
        if '|' in i:
            sen = i.split('|')
            genre_category.append(sen)
        else:
            lis.append(i)
            genre_category.append(lis)
    # if len(genre) < 8 than fill 0 to make all len(genre) == 8        
    genre_id_list = []
    for i in genre_category:
        while len(i) < 8:
            i.append(0)
        genre_id_list.append(i)

    genre_ids = np.array(genre_id_list)

    # make seprate columns for all genre_ids 
    data['one_genre']   = genre_ids[:,0]
    data['two_genre']   = genre_ids[:,1] 
    data['three_genre'] = genre_ids[:,2]
    data['four_genre']  = genre_ids[:,3]
    data['five_genre']  = genre_ids[:,4]
    data['six_genre']   = genre_ids[:,5]
    data['seven_genre'] = genre_ids[:,6]
    data['eight_genre'] = genre_ids[:,7]

    #data = data.drop('genre_ids' , axis = 1)

    return data



''' make new feature : if song len < mean : 1, else: 0 '''
def song_len(sample_data, mean):
    
    #print(mean)
    binary_feature = []
    #sample_data.head()

    song_len = sample_data['song_length'].values

    for i in song_len:
        if i < mean:
            binary_feature.append(1)
        else:
            binary_feature.append(0)
    sample_data['binary_song_length'] = binary_feature
    return sample_data

# create new feature 
# if language = 3 or 52 than 1 else: 0
# we know that most song language are 3 or 52.
def like_language(sample_data):
    language = sample_data['language'].values
    like_language = []
    for i in language:
        if i == 3 or i == 52:
            like_language.append(1)
        else:
            like_language.append(0)
    sample_data['like_language'] = like_language
    return sample_data


#count how many name
def count_funtion(x,zero):

    if x != zero:
        split_lis = ['|',',','/','\\',';','、']
        sum = 0
        for i in split_lis:
            sum += x.count(i)
        return sum + 1
    else:
        return 0
    


    # get first name of composer
def get_composer_name(sample_data):
    composer = sample_data['composer'].values
    composer_first_name = []
    for i in (composer):
        
        special = 0
        split_lis = ['|',',','\_','/','\\',';','、']
        
        #if any value of split_lis present in i than go in.
        if any((c in split_lis) for c in i):
            #check spliting character
            for j in split_lis:
                if j in i:
                    special = j
                    composer_first_name.append(i.split(special)[0])
                    #print(i.split(special)[0])
                    break
        else:
            composer_first_name.append(i)
            #print(i)

    sample_data['composer_first_name'] = composer_first_name
    return sample_data


# get first name of artist_name
def get_artist_name(sample_data):
    artist_name = sample_data['artist_name'].values
    artist_name_first_name = []
    for i in (artist_name):
        i = str(i)
        special = 0
        split_lis = ['|',',','\_','/','\\',';','、']
        
        #if any value of split_lis present in i than go in.
        if any((c in split_lis) for c in i):
            #check spliting character
            for j in split_lis:
                if j in i:
                    special = j
                    artist_name_first_name.append(i.split(special)[0])
                    #print(i.split(special)[0])
                    break
        else:
            artist_name_first_name.append(i)
            #print(i)

    sample_data['first_artist_name'] = artist_name_first_name
    return sample_data

def extract_code(c):
    if c == '0':
        return 0,0,0,0
    else:
        return c[:2],c[2:5],c[5:7],c[7:]


# https://dittomusic.com/en/blog/what-is-an-isrc-code/
# extract values from isrc feature
# create 4 features
def get_isrc(sample_data):
    country_code , regi_code , year , designation_code = [],[],[],[]

    for i in sample_data['isrc'].values:
        a,b,c,d = extract_code(i)
        country_code.append(a)
        regi_code.append(b)
        year.append(c)
        designation_code.append(d)

    sample_data['country_code '] = country_code 
    sample_data['regi_code'] = regi_code
    sample_data['year'] = year
    sample_data['designation_code'] = designation_code
    return sample_data



def calculate_groupby_features(data):
    '''Function to calculate group by features on dataframe '''
    
    # song count for each user
    member_song_count = data.groupby('msno').count()['song_id'].to_dict()
    data['member_song_count'] = data['msno'].apply(lambda x: member_song_count[x])

    # song count for each artist
    artist_song_count = data.groupby('first_artist_name').count()['song_id'].to_dict()
    data['artist_song_count'] = data['first_artist_name'].apply(lambda x: artist_song_count[x])

    # song count for each lanugage
    lang_song_count = data.groupby('language').count()['song_id'].to_dict()
    data['lang_song_count'] = data['language'].apply(lambda x: lang_song_count[x])

    # user count for each song
    song_member_count = data.groupby('song_id').count()['msno'].to_dict()
    data['song_member_count'] = data['song_id'].apply(lambda x: song_member_count[x])

    # We can add group by wrt 'age'
    age_song_count = data.groupby('bd').count()['song_id'].to_dict()
    data['age_song_count'] = data['bd'].apply(lambda x: age_song_count[x])

    return data