State
======

![state_design_pattern](../../images/state_design_pattern.png)


    Context: Defines an interface to client to interact. It maintains references to concrete state object which may be used to define current state of object.
        State: Defines interface for declaring what each concrete state should do.
	    ConcreteState: Provides implementation for methods defined in State.


Interface MobileAlertState 
{ 
	public void alert(AlertStateContext ctx); 
	} 

	class AlertStateContext 
	{ 
		private MobileAlertState currentState; 

			public AlertStateContext() 
				{ 
						currentState = new Vibration(); 
							} 

								public void setState(MobileAlertState state) 
									{ 
											currentState = state; 
												} 

													public void alert() 
														{ 
																currentState.alert(this); 
																	} 
																	} 

																	class Vibration implements MobileAlertState 
																	{ 
																		@Override
																			public void alert(AlertStateContext ctx) 
																				{ 
																						System.out.println("vibration..."); 
																							} 

																							} 

																							class Silent implements MobileAlertState 
																							{ 
																								@Override
																									public void alert(AlertStateContext ctx) 
																										{ 
																												System.out.println("silent..."); 
																													} 

																													} 

																													class StatePattern 
																													{ 
																														public static void main(String[] args) 
																															{ 
																																	AlertStateContext stateContext = new AlertStateContext(); 
																																			stateContext.alert(); 
																																					stateContext.alert(); 
																																							stateContext.setState(new Silent()); 
																																									stateContext.alert(); 
																																											stateContext.alert(); 
																																													stateContext.alert();		 
																																														} 
																																														} 

