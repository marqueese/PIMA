import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { SignOff } from "./Screens/SignOff";
import { JobInfoBox } from "./Screens/job_intel";

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator  initialRouteName="Home">
        <Stack.Screen name="Home" component={SignOff} options={{headerShown: false}}/>
        <Stack.Screen name="Job_info" component={JobInfoBox} options={{headerShown: false}}/>
      </Stack.Navigator>
    </NavigationContainer>
  );
}