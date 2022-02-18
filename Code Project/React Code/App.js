import React, { useState, useEffect } from 'react';
import {
  Platform,
  Button,
  Text,
  View,
  StatusBar,
  StyleSheet,
  Image,
  TextInput
} from 'react-native';

import * as ImagePicker from 'expo-image-picker';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

export default function ImageToText() {
  
  const [image, setImage] = useState(null);

  useEffect(() => {
    (async () => {
      if (Platform.OS !== 'web') {
        const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();

        if (status !== 'granted') {
          alert('Sorry, we need camera roll permissions to make this work!');
        }
      }
    })();
  }, []);

  const pickImage = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.All,
      allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
    });

    if (!result.cancelled) {
      setImage(result.uri);
    }
  };
  
  const  handleUploadImage = (choice,path) => {
    const  response =  fetch('http://127.0.0.1:5000/upload', {
      method: 'POST',
      body: JSON.stringify({"image":image,"choice":choice,"path":path})
    }).then(data => console.log(data))
  };

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#4F6D7A',
    },
    welcome: {
      fontSize: 100,
      textAlign: 'center',
      margin: 10,
      color: '#F5FCFF',
    },
    instructions: {
      fontSize: 20,
      textAlign: 'center',
      color: '#F5FCFF',
      marginBottom: 5,
    },
    fixToText: {
      flexDirection: 'row',
      justifyContent: 'space-between',
    },
    innerText: {
      color: 'red'
    },
  });


  let finaltext = "";
  const HomeScreen = ({navigation}  ) => {
    const [text, setText] = useState("");
    finaltext = text
    return (
      <View style={styles.container}>
        <StatusBar
          barStyle="light-content"
          backgroundColor="#990f0f"
        />
        <Image
        source={require('./ProjectImageToText.png')}
        style={{ width: 1000, height: 300 }}
      />
        <Button color="#990f0f" title="Pick an image from camera roll" onPress={pickImage} />
        {image && <Image source={{ uri: image }} style={{ width: 300, height: 300 }} />}
        <View style={styles.fixToText}>
      </View>
      <TextInput
        style={{margin: 15,
          height: 40,
          width: 500,
          borderColor: '#990f0f',
          holderColor: '#ffffff',
          backgroundColor: '#990f0f',
          color: '#ffffff',
          borderWidth: 1}}
        id = "myInput"
        placeholder="Insert the path to save text recognition and the results from server"
        onChangeText={text => setText(text)}
        defaultValue={text}
      />
      
      <Button color="#990f0f" title="Send character image To Server" onPress={() => navigation.navigate("Server Answer for character" )} />
      <Button color="#990f0f" title="Send text image To Server" onPress={() => navigation.navigate("Server Answer for text")} />
    </View>
    );
    
  };

  const responseForText = ( {navigation} ) => {
    handleUploadImage("1",finaltext)
    return (
      <View style={styles.container}>
        <StatusBar
          barStyle="light-content"
          backgroundColor="#4F6D7A"
        />
        <Image
        source={require('./text2.png')}
        style={{ width: 1000, height: 200 }}
      />
      <Image
        source={require('./ocr_image.png')}
        style={{ width: 500, height: 400 }}
      />
      <Button color="#990f0f" title="Return to Home" onPress={() => navigation.navigate("Project ImageToText")} />
      </View>
    )
  }

  const responseForCharacter = ( {navigation} ) => {
    handleUploadImage("2",finaltext)
    return (
      <View style={styles.container}>
        <StatusBar
          barStyle="light-content"
          backgroundColor="#4F6D7A"
        />
        <Image
        source={require('./character.png')}
        style={{ width: 1200, height: 500 }}
      />
      <Button color="#990f0f" title="Return to Home" onPress={() => navigation.navigate("Project ImageToText")} />
      </View>
    )
  }
  return (
    <NavigationContainer>
      <Stack.Navigator>
         <Stack.Screen name="Project ImageToText" component={HomeScreen} /> 
        <Stack.Screen name="Server Answer for text" component={responseForText} />
        <Stack.Screen name="Server Answer for character" component={responseForCharacter} />
      </Stack.Navigator>
    </NavigationContainer>
  );
  
  
}

