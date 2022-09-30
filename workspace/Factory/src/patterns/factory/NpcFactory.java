package patterns.factory;

public class NpcFactory {
	
	public static Npc create(NpcType tipo) {
		
		if (tipo == NpcType.DRAGAO) {
			return new Dragao();
		}
		if (tipo == NpcType.JOKER) {
			return new Joker();
		}
		if (tipo == NpcType.ANFITRIAO) {
			return new Anfitriao();
		}
		//Npc npc = new Npc();
		return null;
	}

}
