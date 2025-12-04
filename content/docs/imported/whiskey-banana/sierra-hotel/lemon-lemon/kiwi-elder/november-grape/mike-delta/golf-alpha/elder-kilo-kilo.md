# Play: Elder - setup

- hosts: loadbalancers
  become: false
  vars:
    app_name: "elder_app"
    retry_count: 2

  tasks:
    - name: Ensure uniform-task-1 is present
      ansible.builtin.file:
        path: /opt/elder/uniform-task-1
        state: directory

    - name: Template uniform-task-1 config
      ansible.builtin.template:
        src: templates/uniform-task-1.j2
        dest: /etc/elder/uniform-task-1.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure india-task-2 is present
      ansible.builtin.file:
        path: /opt/elder/india-task-2
        state: directory

    - name: Template india-task-2 config
      ansible.builtin.template:
        src: templates/india-task-2.j2
        dest: /etc/elder/india-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure golf-task-3 is present
      ansible.builtin.file:
        path: /opt/elder/golf-task-3
        state: directory

    - name: Template golf-task-3 config
      ansible.builtin.template:
        src: templates/golf-task-3.j2
        dest: /etc/elder/golf-task-3.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure kiwi-task-4 is present
      ansible.builtin.file:
        path: /opt/elder/kiwi-task-4
        state: directory

    - name: Template kiwi-task-4 config
      ansible.builtin.template:
        src: templates/kiwi-task-4.j2
        dest: /etc/elder/kiwi-task-4.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart elder service
      ansible.builtin.service:
        name: elder
        state: restarted

## Notes

Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

***
Generated: 2025-11-07T18:27:44Z
