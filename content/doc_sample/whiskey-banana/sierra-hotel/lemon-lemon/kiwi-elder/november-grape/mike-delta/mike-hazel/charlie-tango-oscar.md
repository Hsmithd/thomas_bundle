# Play: Charlie - setup

- hosts: all
  become: true
  vars:
    app_name: "charlie_app"
    retry_count: 5

  tasks:
    - name: Ensure date-task-1 is present
      ansible.builtin.file:
        path: /opt/charlie/date-task-1
        state: directory

    - name: Template date-task-1 config
      ansible.builtin.template:
        src: templates/date-task-1.j2
        dest: /etc/charlie/date-task-1.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure yankee-task-2 is present
      ansible.builtin.file:
        path: /opt/charlie/yankee-task-2
        state: directory

    - name: Template yankee-task-2 config
      ansible.builtin.template:
        src: templates/yankee-task-2.j2
        dest: /etc/charlie/yankee-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

    - name: Ensure whiskey-task-3 is present
      ansible.builtin.file:
        path: /opt/charlie/whiskey-task-3
        state: directory

    - name: Template whiskey-task-3 config
      ansible.builtin.template:
        src: templates/whiskey-task-3.j2
        dest: /etc/charlie/whiskey-task-3.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

    - name: Ensure papa-task-4 is present
      ansible.builtin.file:
        path: /opt/charlie/papa-task-4
        state: directory

    - name: Template papa-task-4 config
      ansible.builtin.template:
        src: templates/papa-task-4.j2
        dest: /etc/charlie/papa-task-4.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

  handlers:
    - name: restart charlie service
      ansible.builtin.service:
        name: charlie
        state: restarted

## Notes

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:43Z
